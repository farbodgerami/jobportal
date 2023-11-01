/* eslint-disable react-hooks/exhaustive-deps */
import React, { useContext, useEffect, useState } from "react";
import JobContext from "../../context/JobContext";
import { toast } from "react-toastify";
import {
  educationOptions,
  experienceOptions,
  indutriesOptions,
  jobTypeOptions,
} from "./data";
const NewJob = ({ access_token }) => {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [email, setEmail] = useState("");
  const [address, setAddress] = useState("");
  const [jobType, setJobType] = useState("Permanent");
  const [education, setEduction] = useState("Bachelors");
  const [industry, setIndustry] = useState("business");
  const [experience, setExperientce] = useState("No Experience");
  const [salary, setSalay] = useState("");
  const [positions, setPositions] = useState("");
  const [company, setCompany] = useState("");

  const { clearErrors, error, loading,created,createNewJob,setCreated } = useContext(JobContext);
  useEffect(() => {
    if (error) {
      toast.error(error);
      clearErrors();
    }
    if(created){
      setCreated(false)
      toast.success('Job Posted successfully.')
    }
  }, [error,created]);
  const submitHandler = (e) => {
    e.preventDefault();
    const data = {
      title,
      description,
      email,
      address,
      jobType,
      education,
      industry,
      experience,
      salary,
      positions,
      company,
    };
    createNewJob(data,access_token)
  };
  return (
    <div className="newJobcontainer">
      <div className="formWrapper">
        <div className="headerWrapper">
          <div className="headerLogoWrapper"></div>
          <h1>
            <i aria-hidden className="fas fa-copy mr-2"></i> POST A JOB
          </h1>
        </div>
        <form className="form" onSubmit={submitHandler}>
          <div className="row">
            <div className="col-12 col-md-6">
              <div className="inputWrapper">
                <div className="inputBox">
                  <i aria-hidden className="fab fa-tumblr"></i>
                  <input
                    type="text"
                    placeholder="Enter Job Title"
                    required
                    value={title}
                    onChange={(e) => {
                      setTitle(e.target.value);
                    }}
                  />
                </div>
                <div className="inputBox">
                  <i aria-hidden className="fas fa-file-medical-alt"></i>
                  <textarea
                    className="description"
                    type="text"
                    placeholder="Enter Job Description"
                    required
                    value={description}
                    onChange={(e) => {
                      setDescription(e.target.value);
                    }}
                  />
                </div>
                <div className="inputBox">
                  <i aria-hidden className="fas fa-envelope"></i>
                  <input
                    type="email"
                    placeholder="Enter Your Email"
                    pattern="\S+@\S+\.\S+"
                    title="Your email is invalid"
                    required
                    value={email}
                    onChange={(e) => {
                      setEmail(e.target.value);
                    }}
                  />
                </div>
                <div className="inputBox">
                  <i aria-hidden className="fas fa-map-marker-alt"></i>
                  <input
                    type="text"
                    placeholder="Enter Address"
                    required
                    value={address}
                    onChange={(e) => {
                      setAddress(e.target.value);
                    }}
                  />
                </div>
                <div className="inputBox">
                  <i aria-hidden className="fas fa-dollar-sign"></i>
                  <input
                    type="number"
                    placeholder="Enter Salary Range"
                    required
                    value={salary}
                    onChange={(e) => {
                      setSalay(e.target.value);
                    }}
                  />
                </div>
                <div className="inputBox">
                  <i aria-hidden className="fas fa-users"></i>
                  <input
                    type="number"
                    placeholder="Enter No. of Positions"
                    required
                    value={positions}
                    onChange={(e) => {
                      setPositions(e.target.value);
                    }}
                  />
                </div>
                <div className="inputBox">
                  <i aria-hidden className="fas fa-building"></i>
                  <input
                    type="text"
                    placeholder="Enter Company Name"
                    required
                    value={company}
                    onChange={(e) => {
                      setCompany(e.target.value);
                    }}
                  />
                </div>
              </div>
            </div>
            <div className="col-12 col-md-6 ml-4 mt-4 mt-md-0 ml-md-0">
              <div className="boxWrapper">
                <h4>Job Types:</h4>
                <div className="selectWrapper">
                  <select
                    value={jobType}
                    onChange={(e) => {
                      setJobType(e.target.value);
                    }}
                    className="classic"
                  > 
                    {jobTypeOptions.map((option) => {
                      return<option key={option} value={option}>{option}</option>;
                    })}
                  </select>
                </div>
              </div>

              <div className="boxWrapper">
                <h4>Education:</h4>
                <div className="selectWrapper">
                  <select
                    value={education}
                    onChange={(e) => {
                      setEduction(e.target.value);
                    }}
                    className="classic"
                  >
                    {educationOptions.map((option) => {
                  return    <option key={option} value={option}>{option}</option>;
                    })}
                  </select>
                </div>
              </div>

              <div className="boxWrapper">
                <h4>Industry:</h4>
                <div className="selectWrapper">
                  <select
                    value={industry}
                    onChange={(e) => {
                      setIndustry(e.target.value);
                    }}
                    className="classic"
                  >
                    {indutriesOptions.map((option) => {
                     return <option key={option} value={option}>{option}</option>;
                    })}
                  </select>
                </div>
              </div>

              <div className="boxWrapper">
                <h4>Experience:</h4>
                <div className="selectWrapper">
                  <select
                    value={experience}
                    onChange={(e) => {
                      setExperientce(e.target.value);
                    }}
                    className="classic"
                  >
                    {experienceOptions.map((option) => {
                    return  <option key={option} value={option}>{option}</option>;
                    })}
                  </select>
                </div>
              </div>
            </div>

            <div className="col text-center mt-3">
              <button className="createButton">
                {loading ? "posting..." : "Create Job"}
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  );
};

export default NewJob;
