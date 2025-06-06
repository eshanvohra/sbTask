const mongoose = require("mongoose");

var jobsSchema = new mongoose.Schema({
  job_Name: {
    type: String,
    required: true,
    maxLength: 32,
    trim: true,
  },
  description: {
    type: String,
    trim: true,
    required: true,
    unique: true,
  },
  experience: {
    type: String,
    required: true,
  },
   postedBy: {
    type: String,
    required: true,
  },
  applied_by:{
    type:Array
  }
},
{timestamps:true}
);




module.exports = mongoose.model("Jobs", jobsSchema);
