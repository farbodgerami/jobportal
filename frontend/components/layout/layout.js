/* eslint-disable @next/next/no-before-interactive-script-outside-document */
import React from "react";
import Head from "next/head";
import Script from "next/script";
import Header from "./Header";
import Footer from "./Footer";
import { ToastContainer } from "react-toastify";
import 'react-toastify/dist/ReactToastify.css'
const Layout = ({ title = "Find Your Jb Now", children }) => {
  return (
    <>
      <Head>
        <title>{title} - jobbie</title>
      </Head>
<ToastContainer position="bottom-center"/>
      <Header />

      {children}
      <Footer />
    </>
  );
};

export default Layout;
