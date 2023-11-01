import React from 'react'
import axios from 'axios'
import JobCandidates from '../../../../components/job/JobCandidates'
import Layout from '../../../../components/layout/layout'
import NotFound from '../../../../components/layout/NotFound'
import { isAuthenticatedUser } from "../../../../utils/isAuthenticated"
const JobCandidatesPage = ({candidatesApplied,error}) => {

 
  if(error==="Not found.") return <NotFound/>
 
  return (
<Layout title = "Job Condidates">
    <JobCandidates candidatesApplied={candidatesApplied}  />
</Layout>
  )
}

export default JobCandidatesPage




export async function getServerSideProps({req,params}){
    const access_token = req.cookies.access;
    const user = await isAuthenticatedUser(access_token);
    if(user===false){
        return{
            redirect:{
                destination:'/login',permanent:false
            }
        }
    }
    try {
      const res = await axios.get(`${process.env.API_URL}/apii/jobs/${params.id}/candidate/`,{headers:{Authorization:`Bearer ${access_token}`}})
      const candidatesApplied=res.data
    

 


    return {
        props:{candidatesApplied}
    }
  } catch (error) {
    // console.log(error.response.statusText)
  return{

    props:{error:error.response.statusText}
  }
  }
}