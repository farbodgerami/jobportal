
import axios from "axios";
import Layout from "../../components/layout/layout";
import JobApplied from "../../components/job/jobApplied";
import { isAuthenticatedUser } from "../../utils/isAuthenticated";
export default function JobsAppliedPage({ jobs }) {
console.log(jobs)
  return (
    <Layout title="Jobs Applied">
<JobApplied jobs={jobs}/>
    </Layout>
  );
}

export async function getServerSideProps({ req }) {
 
    const access_token = req.cookies.access;
  
    const user = await isAuthenticatedUser(access_token);
    if(user===false){
        return{
            redirect:{
                destination:'/login',permanent:false
            }
        }
    }

    const res = await axios.get(`${process.env.API_URL}/apii/me/jobs/applied`,{headers:{Authorization: `Bearer ${access_token}`}})
const jobs=res.data
 
    return {
      props: {jobs
    },
    };
  }
 
