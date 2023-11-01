import React from "react";
import Filters from "./layout/Filters";
import JobItem from "./job/JobItem";
import Link from "next/link";
import { useRouter } from "next/router";
import Pagination from "react-js-pagination";

const Home = ({ data }) => {
  const router = useRouter();
  // http://localhost:3000/?keyword=va&location=ertgh&r=fghn
  // console.log(router.query)
  // {keyword: 'va', location: 'ertgh', r: 'fghn'}
  // console.log(router);
  let { keyword, page = 1 } = router.query;
  // to highlight numbers:
  page = Number(page);
  const { jobs, count, resPerPage } = data;
  let queryParams;
  if (typeof window !== "undefined") {
    queryParams = new URLSearchParams(window.location.search);
  }
  const handlePageClick = (currentPage) => {
    // console.log(window.location.search)//?page=1&lodcation=aaa
    // console.log("llllllllllllll",new URLSearchParams(window.location.search))
    if (queryParams.has("page")) {
      queryParams.set("page", currentPage);
    } else {
      queryParams.append("page", currentPage);
    }
    // console.log(queryParams.toString())//page=1
    router.push({ search: queryParams });
    // let url = window.location.search;
    // console.log(url)
    // if (url.includes("?page=")) {
    //   const a="?page=".substring(5.0)
    //   console.log(a)
    //   url.replace(a,currentPage)
    // } else if(url.includes("&page=")) {
    //   url.replace()
    // }else{
    //   url=url.concat(`?page=${currentPage}`)

    // }
    // router.push(url);
  };
  return (
    <>
      <div className="container container-fluid">
        <div className="row">
          <div className="col-xl-3 col-lg-4">
            <Filters />{" "}
          </div>

          <div className="col-xl-9 col-lg-8 content-left-offset">
            <div className="my-5">
              <h4 className="page-title">
                {keyword
                  ? `${jobs.length} Results for ${keyword}`
                  : "latest Jobs"}
              </h4>
              <Link href="/stats">
                <button className="btn btn-secondary float-right stats_btn">
                  Get Topic stats
                </button>
              </Link>
              <div className="d-block">
                <Link href="/search">Go to Search</Link>
              </div>
            </div>
            {jobs && jobs.map((job) => <JobItem key={job.id} job={job} />)}
            {resPerPage < count && (
              <div className="d-flex justify-content-center mt-5">
                <Pagination
                  activePage={page}
                  itemsCountPerPage={resPerPage}
                  totalItemsCount={count}
                  onChange={handlePageClick}
                  nextPageText={"Next"}
                  prevPageText={"Back"}
                  firstPageText={"First"}
                  lastPageText={"Last"}
                  itemClass="page-item"
                  linkClass="page-link"
                />
              </div>
            )}
          </div>
        </div>
      </div>
    </>
  );
};

export default Home;
