import React from 'react'
import axios from 'axios'
import UpdateJob from '../../../components/job/UpdateJob'
import NotFound from '../../../components/layout/NotFound'
import Layout from '../../../components/layout/layout'

import { isAuthenticatedUser } from "../../../utils/isAuthenticated"

const UpdateJobPage = ({job,access_token,error}) => {
 
  if(error==="Not found.") return <NotFound/>
 
  return (
<Layout title = "Job Condidates">
    <UpdateJob job={job} access_token={access_token}  />
</Layout>
  )
}

export default UpdateJobPage




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
      const res = await axios.get(`${process.env.API_URL}/apii/jobs/${params.id}/`)
      const job=res.data.job
    

 


    return {
        props:{job,access_token}
    }
  } catch (error) {
    // console.log(error.response.statusText)
  return{

    props:{error:error.response.statusText}
  }
  }
}