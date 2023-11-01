import axios from "axios";

export const isAuthenticatedUser = async (access_token) => {
  console.log('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj',access_token)
  try {
    const response = await axios.post(
      `${process.env.API_URL}/apii/token/verify/`,
      { token: access_token }
    );
    console.log('gggggggggggggggggggggggggggggggggggggggggggggggggggg',response)
    if (response.status == 200) {
      return true;
    }
  } catch (error) {
    return false;
  }
};
