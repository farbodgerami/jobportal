import Link from "next/link";
import React from "react";
import DataTable from "react-data-table-component";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
const jobApplied = ({ jobs }) => {
  const columns = [
    { name: "Job name", sortable: true, selector: (row) => row.title },
    { name: "Salary", sortable: true, selector: (row) => row.salary },
    { name: "Education", sortable: true, selector: (row) => row.education },
    { name: "Experience", sortable: true, selector: (row) => row.experience },
    { name: "Applied On", sortable: true, selector: (row) => row.applieOn },
    { name: "Action", sortable: true, selector: (row) => row.action },
  ];
  const data = [];
  console.log(jobs)
  jobs &&
    jobs.forEach((item) => {
      data.push({
        title: item.job.title,
        salary: item.job.salary,
        education: item.job.education,
        experience: item.job.experience,
        applieOn: item.appliedAt.substring(0, 10),
        action: <Link className="btn btn-primary p-0 pl-2 pr-2 " href={`/job/${item.job.id}`}>
          job
        {/* <i aria-hidden className="fa fa-eye"></i> */}
 
        </Link>,
      });
    });
  return (
 
    <div className="row">
      <div className="col-2"></div>
      <div className="col-8 mt-5">
        <h4 className="my-5">Jobs Applied</h4>
        <DataTable columns={columns} data={data} pagination responsive/>
      </div>
      <div className="col-2"></div>
    </div>
  );
};

export default jobApplied;
