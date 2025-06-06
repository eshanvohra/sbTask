const mongoose = require("mongoose");

var candidateSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    maxLength: 32,
    trim: true,
  },
  email: {
    type: String,
    trim: true,
    required: true,
    unique: true,
  },
  password: {
    type: String,
    required: true,
  },
  appliedJobs: {
    type: Array
  },
   experience: {
    type: Number,
    default: 0,
  }
},
{timestamps:true}
);

candidateSchema.methods = {
    authenticate: function (password) {
      return password===this.password  
    }
};


module.exports = mongoose.model("Candidate", candidateSchema);
