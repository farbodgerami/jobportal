 
import Layout from "../../../components/layout/layout";
 import NewJob from "../../../components/job/NewJob";
import { isAuthenticatedUser } from "../../../utils/isAuthenticated";
export default function JobsAppliedPage({ access_token }) {
 
  return (
    <Layout title="post a NewJob">
<NewJob access_token={access_token}/>
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
 
 
 
    return {
      props: {access_token
    },
    };
  }
 
