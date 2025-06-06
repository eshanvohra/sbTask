const express = require("express");
const Candidate = require("../models/candidate");
const jobs = require("../models/jobs");
const router = express.Router();
const JWT_KEY="thisissecret"
const jwt = require('jsonwebtoken');

const validate=require('./validate')

router.post("/candidate/login", async (req, res) => {
    try {
        const { email, password } = req.body;

        if (!email || !password) {
            return res.status(400).json({ message: "Email and password are required." });
        }
        const candidate = await Candidate.findOne({ email });
        if (!candidate) {
            return res.status(401).json({ message: "Invalid email or password." });
        }
        const isMatch = password==candidate.password;
        if (!isMatch) {
            return res.status(401).json({ message: "Invalid email or password." });
        }

        const payload = {
            userId: candidate._id,
            role: "candidate",
            email: candidate.email,
        };

        const token = jwt.sign(payload, JWT_KEY, { expiresIn: '1h' });

        return res.status(200).json({
            message: "Login successful",
            token,
        });
    } catch (err) {
        console.error("Login Error:", err);
        return res.status(500).json({ message: "Server error", error: err.message });
    }
});

router.post("/candidate/signup", async (req, res) => {
    try {
        const { name, email, password } = req.body;

        if (!name || !email || !password) {
            return res.status(400).json({ error: "Name, email, and password are required." });
        }

        const candidate = new Candidate({ name, email, password });


        const savedCandidate = await candidate.save();

        res.status(201).json({
            name: savedCandidate.name,
            email: savedCandidate.email,
            id: savedCandidate._id,
        });

    } catch (err) {
        console.error("Signup error:", err);


        return res.status(400).json({
            error: "Sorry, but this user already exists!",
        });


    }
})

router.get("/listJobs", async (req, res) => {
    try {

        const allJobs = await jobs.find();

        res.status(200).json({
            message: "success",
            jobs: allJobs,
        });
    } catch (err) {
        console.error("Error listing jobs:", err);
        res.status(500).json({
            error: "Internal server error",
        });
    }
});


router.post("/candidate/applyJob",validate, async (req, res) => {
    try {
        const { candidate_id, job_id } = req.body;

        if (!candidate_id || !job_id) {
            return res.status(400).json({ error: "Mandatory params are missing to apply for job" });
        }

        const candidate = await Candidate.findById(candidate_id);
        if (!candidate) {
            return res.status(404).json({ error: "Candidate not found" });
        }
        const job = await jobs.findById(job_id);
        if (!job) {
            return res.status(404).json({ error: "Job not found" });
        }

        if (candidate.appliedJobs.includes(job_id)) {
            return res.status(409).json({ error: "Candidate already applied to this job" });
        }

        candidate.appliedJobs.push(job_id);
        await candidate.save();

        job.applied_by.push(candidate_id);
        await job.save();
        res.status(200).json({
            message: "Job applied successfully",
            appliedJobs: candidate.appliedJobs,
        });

    } catch (err) {
        console.error("Error applying for job:", err);
        res.status(500).json({ error: "Internal server error" });
    }
});


router.post("/candidate/listJobs",validate, async (req, res) => {
    try {
        const { candidate_id } = req.body;

        if (!candidate_id) {
            return res.status(400).json({ error: "Mandatory params are missing" });
        }
        const candidate = await Candidate.findById(candidate_id);
        if (!candidate) {
            return res.status(404).json({ error: "Candidate not found" });
        }
//            const allJobs = await jobs.find();
// console.log(allJobs);
// const jobsWithNames=candidate.appliedJobs.map((job_id)=>{

// })

        res.status(200).json({
            message: `Jobs applied by candidate: ${candidate.name}`,
            appliedJobs: candidate.appliedJobs,
        });
    }
    catch (err) {
        res.status(500).json(err)
    }

});

// router.post("/candidate/sendMail", async (req, res) => {
//     try {

//         res.status(200).json({
//             "message": "success"
//         })
//     }
//     catch (err) {
//         res.status(500).json(err)
//     }

// });
// router.post("/candidate/logout", async (req, res) => {
//     try {

//         res.status(200).json({
//             "message": "success"
//         })
//     }
//     catch (err) {
//         res.status(500).json(err)
//     }

// });

module.exports = router;
