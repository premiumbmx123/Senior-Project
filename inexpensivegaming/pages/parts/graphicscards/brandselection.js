import styles from '../../../styles/Home.module.css'
import Link from 'next/link'
import Head from 'next/head'

export default function parts() {
  return (
    <div>
      <Head>
        <title>Inexpensive Gaming</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/ie.ico" />
      </Head>

      <div className={styles.bar}>
        <Link href="/">
          <a>
            <h2>Inexpensive Gaming</h2>
          </a>
        </Link>

        <div className={styles.links}>
          <Link href="/parts">
            <a>
              <h3>Parts</h3>
            </a>
          </Link>

          <Link href="/buildguide">
            <a>
              <h3>Build Guide</h3>
            </a>
          </Link>

          <Link href="/benchmarks">
            <a>
              <h3>Benchmarks</h3>
            </a>
          </Link>
        </div>
      </div>

      <main className={styles.main}>
        <div>
          <h2 className={styles.title}>What brand are you looking for?</h2>
        </div>

        <div className={styles.grid}>
          <Link href="/parts/graphicscards/nvidia-graphics-cards">
            <a className={styles.card}>
              <h2>NVIDIA</h2>
            </a>
          </Link>

          <Link href="/parts/graphicscards/amd-graphics-cards">
            <a className={styles.card}>
              <h2>AMD</h2>
            </a>
          </Link>
        </div>
      </main>
    </div>
  )
}