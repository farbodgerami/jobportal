/* eslint-disable @next/next/no-before-interactive-script-outside-document */
import Head from "next/head";
import Image from "next/image";
import styles from "../styles/Home.module.css";
import Link from "next/link";
import Layout from "../components/layout/layout";
import Home from "../components/Home";
import Script from "next/script";
import axios from "axios";
export default function Index({ data }) {
  // console.log("jobs",data)
  return (
    <div className={styles.container}>
      <Layout>
        <Home data={data} />
      </Layout>
    </div>
  );
}

// export async function getServerSideProps({query}) {
export async function getServerSideProps(props) {
  // console.log('yyyyyyyyyyyyyyyy',props) query: { pages: '2' },
  const query = props.query;
  const jobType = query.jobType || "";
  const education = query.education || "";
  const experience = query.experience || "";
  const keyword = query.keyword || "";
  const location = query.location || "";
  const page = query.page || 1;
  let min_salary = "";
  let max_salary = "";
  if (query.salary) {
    const [min, max] = query.salary.split("-");
    min_salary = min;
    max_salary = max;
  }
  // tavajjoh shavad ke agar dar &jobType=${jobType}&jobType=Temporary , ${jobType} khali bashad kollan kar nemikonad pass nabayad kahli bezarish. bayad ba har entekhab ezafe va hazf shavad.
  const queryStr = `keyword=${keyword}&location=${location}&page=${page}&jobType=${jobType}&education=${education}&experience=${experience}&min_salary=${min_salary}&max_salary=${max_salary}`;
  let data="";
  try {
    const res = await axios.get(`${process.env.API_URL}/apii/jobs?${queryStr}`);
     data = res.data;
    
  } catch (error) {
    console.log(error)
  }
  return {
    props: {
      data,
    },
  };
}
 