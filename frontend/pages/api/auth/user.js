/* eslint-disable import/no-anonymous-default-export */
import axios from "axios";
import cookie from "cookie";

export default async (req, res) => {
  if (req.method === "GET") {
    const cookies = cookie.parse(req.headers.cookie || "");
    const access = cookies.access || false;
    if (!access) {
      return res.status(401).json({ message: "Login first to load user" });
    }
    try {
      const response = await axios.get(
        `${process.env.API_URL}/apii/account/me/`,
 

        { headers: { Authorization: `Bearer ${access}` } }
      );
      if(response.data){
        return res.status(200).json({user:response.data})
      }
    } catch (error) {
 

      return res.status(error?.response.status).json({
        error: "Somthing went wrong while retrieving user",
      });
    }
  }
};
