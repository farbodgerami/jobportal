/* eslint-disable @next/next/no-before-interactive-script-outside-document */

import styles from '../styles/Home.module.css'

import Layout from '../components/layout/layout'

import Search from '../components/layout/Search'
export default function Index({ data }) {

    return (

        <Layout title= 'Search your jobs'>
            <Search />
        </Layout>

    )
}


