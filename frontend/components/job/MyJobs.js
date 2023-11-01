/* eslint-disable react-hooks/exhaustive-deps */
import Link from "next/link";
import React, { useEffect ,useContext} from "react";
import DataTable from "react-data-table-component";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import JobContext from "../../context/JobContext";
import { useRouter } from "next/router";
const MyJobs = ({ jobs,access_token }) => {
  const router=useRouter()
  const { clearErrors, error, loading,deleted,deleteJob,setDeleted } = useContext(JobContext);

 useEffect(()=>{
  if(error){
    toast.error(error)
    clearErrors()
  }
  if(deleted){
    setDeleted(false)
    // router.reload(router.asPath)
    router.push(router.asPath)
  }
 },[error,deleted])

 const deleteJobHandler=(id)=>{
deleteJob(id,access_token)
 }
  const columns = [
    { name: "Job ID", sortable: true, selector: (row) => row.id },
    { name: "Job name", sortable: true, selector: (row) => row.title },
    { name: "Salary", sortable: true, selector: (row) => row.salary },
    { name: "Action", sortable: true, selector: (row) => row.action },
  ];
  const data = [];
  // console.log(jobs)
  jobs &&
    jobs.forEach((job) => {
      data.push({
        id: job.id,
        title: job.title,
        salary: job.salary,
        
        action: (
          <>
            <Link
              className="btn btn-primary p-0 pl-2 pr-2 "
              href={`/job/${job.id}`}
            >
              job
            </Link>
            <Link
              className="btn btn-success p-0 pl-2 pr-2 my-1 mx-2 "
              href={`/employeer/jobs/candidates/${job.id}`}
            >
                 {/* <i aria-hidden className="fa fa-users"></i> */}
              user
            </Link>
            <Link
              className="btn btn-warning p-0 pl-2 pr-2 "
              href={`/employeer/jobs/${job.id}`}
            >
                 {/* <i aria-hidden className="fa fa-pen"></i> */}
              edit
            </Link>
            <button onClick={()=>{deleteJobHandler(job.id)}} className="btn btn-danger py-0 mx-1">
              trash
              {/* <i className="fa fa-trash"></i> */}
            </button>
          </>)
      });
    });

  return (
 
    <div className="row">
      <div className="col-2"></div>
      <div className="col-8 mt-5">
        <h4 className="my-5">My Jobs</h4>
        <DataTable columns={columns} data={data} pagination responsive/>
      </div>
      <div className="col-2"></div>
    </div>
  );
};

export default MyJobs;
