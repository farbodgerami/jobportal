import React, { useContext } from "react";
import Link from "next/link";
import Image from "next/image";
import AuthContext from "../../context/AuthContext";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";
const Header = () => {
  const { loading, user,logOutUser } = useContext(AuthContext);
  // console.log(user);
  const logoutHandler=()=>{
    logOutUser()
  }
  // console.log(loading)
  return (
    <div className="navWrapper">
      <div className="navContainer">
        <Link href="/">
          <div className="logoWrapper">
            <div className="logoImgWrapper">
              <Image width="50" height="50" src="/images/logo.png" alt="" />
            </div>
            <span className="logo1">Job</span>
            <span className="logo2">bee</span>
          </div>
        </Link>
        <div className="btnsWrapper">
          <Link href="/employeer/jobs/new">
            <button className="postAJobButton">
              <span>Post A Job</span>
            </button>
          </Link>
          {user ? (

            <div>
              <NavDropdown
                title={`hi ${user.first_name}`}
                id="basic-nav-dropdown"
              >

                <NavDropdown.Item href="/employeer/jobs">
                  My Jobs
                </NavDropdown.Item>
                <NavDropdown.Item legacyBehavior href="/me/applied">
                  Jobs Applied
                </NavDropdown.Item>

                <NavDropdown.Item legacyBehavior href="/me">
                  Profile
                </NavDropdown.Item>
                <NavDropdown.Item legacyBehavior href="/upload/resume">
                  Upload Resume
                </NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item legacyBehavior onClick={logoutHandler}>
                  Logout
                </NavDropdown.Item>
              </NavDropdown>
            </div>
          ) : (
            !loading && (
              <Link href="/login">
                <button className="loginButtonHeader">
                  <span>Login</span>
                </button>
              </Link>
            )
          )}
        </div>
      </div>
    </div>
  );
};

export default Header;
