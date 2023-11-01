import React from 'react'
import axios from 'axios'
import JobDetails from '../../components/job/JobDetails'
import Layout from '../../components/layout/layout'
import NotFound from '../../components/layout/NotFound'

const JobDetailsPage = ({job,candidates,error,access_token}) => {

  // console.log(access_token)
  if(error==="Not found.") return <NotFound/>
  // console.log(error)
  return (
<Layout>
    <JobDetails job={job} candidates={candidates} access_token={access_token}/>
</Layout>
  )
}

export default JobDetailsPage

export async function getServerSideProps({req,params}){
  try {
    
    const res=await axios.get(`${process.env.API_URL}/apii/jobs/${params.id}/`)
    const job=res.data.job
    const candidates=res.data.candidates
const access_token=req.cookies.access || "";
    return {
        props:{job,candidates,access_token}
    }
  } catch (error) {
  return{

    props:{error:error.response.data.detail}
  }
  }
}