import { NextResponse } from "next/server";
const allowdParams=[
    'keyword','location', 'page', 'education' , 'experience' , 'salary' , 'jobType'
]

export async function middleware(req){
    const url=req.nextUrl
 
    let changed= false
    url.searchParams.forEach((param,key)=>{
        if(!allowdParams.includes(key)){
            url.searchParams.delete(key)
            changed=true
        }
    }) 
    if(changed){
        return NextResponse.redirect(url)
    }
}