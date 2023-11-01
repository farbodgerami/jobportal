/* eslint-disable react-hooks/exhaustive-deps */
import axios from "axios";

import { useState, createContext } from "react";
const JobContext = createContext();
export const JobProvider = ({ children }) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [updated, setUpdated] = useState(false);
  const [created, setCreated] = useState(false);
  const [applied, setApplied] = useState(false);
  const [stats, setStats] = useState(null);
  const [deleted, setDeleted] = useState(false);


  const checkJobApplied = async (id, access_token) => {
    // console.log(access_token);
    try {
      setLoading(true);
      const res = await axios.get(
        `/apii/jobs/${id}/check/`,
        {
          headers: {
            Authorization: `Bearer ${access_token}`,
          },
        }
      );
      console.log(res);

      setApplied(res.data);
      setLoading(false);
    } catch (error) {
      setLoading(false);
      setError(
        error.response &&
          (error.response.data.detail || error.response.data.error)
      );
    }
  };
  
  const applyToJob = async (id, access_token) => {
    // console.log(access_token);
    try {
      setLoading(true);
      const res = await axios.post(
        `/apii/jobs/${id}/apply/`,
        {},
        {
          headers: {
            Authorization: `Bearer ${access_token}`,
          },
        }
      );

      if (res.data.applied === true) {
        setApplied(true);
        setLoading(false);
      }
    } catch (error) {
      setLoading(false);
      setError(
        error.response &&
          (error.response.data.detail || error.response.data.error)
      );
    }
  };

  const createNewJob = async (data, access_token) => {
    // console.log(access_token);
    try {
      setLoading(true);
      const res = await axios.post(
        `/apii/jobs/newJob/`,
        data,
        {
          headers: {
            Authorization: `Bearer ${access_token}`,
          },
        }
      );

      if (res.data) {
        setCreated(true);
        setLoading(false);
      }
    } catch (error) {
      setLoading(false);
      setError(
        error.response &&
          (error.response.data.detail || error.response.data.error)
      );
    }
  };

  const updateJob = async (id, data, access_token) => {
    // console.log(access_token);
    try {
      setLoading(true);
      const res = await axios.put(
        `/apii/jobs/${id}/update/`,
        data,
        {
          headers: {
            Authorization: `Bearer ${access_token}`,
          },
        }
      );

      if (res.data) {
        setLoading(false);
        setUpdated(true);
      }
    } catch (error) {
      setLoading(false);
      setError(
        error.response &&
          (error.response.data.detail || error.response.data.error)
      );
    }
  };



  const deleteJob = async (id, access_token) => {
    // console.log(access_token);
    try {
      setLoading(true);
      const res = await axios.delete(
        `/apii/jobs/${id}/delete/`,
        {
          headers: {
            Authorization: `Bearer ${access_token}`,
          },
        }
      );
      console.log(res);

      setDeleted(true);
      setLoading(false);
    } catch (error) {
      setLoading(false);
      setError(
        error.response &&
          (error.response.data.detail || error.response.data.error)
      );
    }
  };
  const getTopicStats = async (topic) => {
    try {
      setLoading(true);
      const res = await axios.get(`/apii/stats/${topic}/`);

      setLoading(false);
      setStats(res.data);
    } catch (error) {
      setLoading(false);
      setError(
        error.response &&
          (error.response.data.detail || error.response.data.error)
      );
    }
  };

  const clearErrors = () => {
    setError(null);
  };
  return (
    <JobContext.Provider
      value={{
        loading,
        // user,
        error,
        deleteJob,
        setApplied,
        setDeleted,
        applyToJob,
        updateJob,
        clearErrors,
        setUpdated,
        checkJobApplied,
        getTopicStats,
        createNewJob,
        setCreated,
        updated,
        deleted,
        stats,
        applied,
        created,
      }}
    >
      {children}
    </JobContext.Provider>
  );
};
export default JobContext;
