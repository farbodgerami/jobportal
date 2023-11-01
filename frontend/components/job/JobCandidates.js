import Link from "next/link";
import React from "react";
import DataTable from "react-data-table-component";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const JobCondidates = ({ candidatesApplied }) => {
  const columns = [
    { name: "Job Name", sortable: true, selector: (row) => row.title },
    { name: "User ID", sortable: true, selector: (row) => row.id },
    { name: "Candidate Resume", sortable: true, selector: (row) => row.resume },
    { name: "Applied At", sortable: true, selector: (row) => row.appliedAt },
  ];
  const data = [];
  // console.log(jobs)
  candidatesApplied &&
    candidatesApplied.forEach((item) => {
      data.push({
        title: item.job.title,
        id: item.user,
        salary: item.salary,

        resume: (
          <>
             <Link className="text-success text-center ml-4" href='#'>View Resume</Link>
          </>
        ),
        appliedAt:item.appliedAt.substring(0,10)
      });
    });
console.log(candidatesApplied)
  return (
    <div className="row">
      <div className="col-2"></div>
      <div className="col-8 mt-5">
        <h4 className="my-5">{candidatesApplied&&`${candidatesApplied.length} Candidates appleid to this job`}</h4>
        <DataTable columns={columns} data={data} pagination responsive />
      </div>
      <div className="col-2"></div>
    </div>
  );
};

export default JobCondidates;
