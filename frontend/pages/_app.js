import { AuthProvider } from "../context/AuthContext";
import "../styles/globals.css";
import { JobProvider } from "../context/JobContext";
import cors from 'cors'
function MyApp({ Component, pageProps }) {

  return (
    <AuthProvider>
      <JobProvider>
        <Component {...pageProps} />
      </JobProvider>
    </AuthProvider>
  );
}

export default MyApp;
