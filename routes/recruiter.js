const express = require("express");
const router = express.Router();
const Recruiter = require("../models/recruiter");
const Jobs = require("../models/jobs");
const Candidate = require("../models/candidate");
const JWT_KEY="thisissecret"
const jwt = require('jsonwebtoken');

const validate=require('./validate')

router.post("/recruiter/login", async (req, res) => {
    try {
        const { email, password } = req.body;

        if (!email || !password) {
            return res.status(400).json({ message: "Email and password are required." });
        }
        const recruiter = await Recruiter.findOne({ email });
        if (!recruiter) {
            return res.status(401).json({ message: "Invalid email or password." });
        }
        const isMatch = password==recruiter.password;
        if (!isMatch) {
            return res.status(401).json({ message: "Invalid email or password." });
        }

        const payload = {
            userId: recruiter._id,
            role: "recruiter",
            email: recruiter.email,
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
router.post("/recruiter/signup", async (req, res) => {
    try {
        const { name, email, password } = req.body;

        if (!name || !email || !password) {
            return res.status(400).json({ error: "Name, email, and password are required." });
        }

        const recruiter = new Recruiter({ name, email, password });


        const savedRecruiter = await recruiter.save();

        res.status(201).json({
            name: savedRecruiter.name,
            email: savedRecruiter.email,
            id: savedRecruiter._id,
        });

    } catch (err) {
        console.error("Signup error:", err);


        return res.status(400).json({
            error: "Sorry, but this user already exists!",
        });


    }
})
router.post("/recruiter/postJob", validate,async (req, res) => {
    try {
        const { job_Name, description, experience, postedBy } = req.body;

        if (!job_Name || !description || !experience || !postedBy) {
            return res.status(400).json({ error: "Mandatory params for posting job are missing" });
        }


        const job = new Jobs({ job_Name, description, experience, postedBy });


        const savedJob = await job.save();

        res.status(201).json({
            name: savedJob.name,
            email: savedJob.email,
            id: savedJob._id,
        });

    } catch (err) {
        console.error("Job posting error error:", err);


        return res.status(400).json({
            error: err.message
        });


    }
})

router.post("/recruiter/listApplicants",validate, async (req, res) => {
    try {
        const { job_id } = req.body;

        if (!job_id) {
            return res.status(400).json({ error: "Mandatory params are missing " });
        }

        const job = await Jobs.findById(job_id);
        const allCandidates = await Candidate.find();

        const applicantsList = job.applied_by.map(candidate_id => {
            const candidate = allCandidates.find(c => c._id.toString() === candidate_id.toString());
            return candidate ? candidate.name : null;
        })

        res.status(200).json({
            "message": "success",
            applicantsList
        })
    }
    catch (err) {
        res.status(500).json(err)
    }

});

// router.post("/recruiter/logout", async (req, res) => {
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
