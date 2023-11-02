/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,

// docker:
  env:{
    API_URL:'http://jobportalbackend:8000',
  },
  async rewrites() {
      return [
          {
              source: '/apii/:path*',
              destination: 'http://jobportalbackend:8000/apii/:path*',
            },
          ]
        },

  
// dev:
        // env:{
        //   API_URL:'http://127.0.0.1:8000',
        // },
         
        // async rewrites() {
        //   return [
        //     {
        //       source: '/apii/:path*',
        //       destination: 'http://127.0.0.1:8000/apii/:path*/',
        //     },
        //   ]
        // },
}

module.exports = nextConfig



