const mongoose = require("mongoose");

var recruiterSchema = new mongoose.Schema({
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
  }
},
{timestamps:true}
);

recruiterSchema.methods = {
    authenticate: function (password) {
      return password===this.password  
    }
};



module.exports = mongoose.model("Recruiter", recruiterSchema);
