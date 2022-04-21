import Head from 'next/head'
import styles from '../../../styles/Home.module.css'
import Link from 'next/link'
import Image from 'next/image'
import { connectToDatabase } from '../../../util/mongodb'

export default function graphicsCards({ parts }) {
  return (
    <div>
      <Head>
        <title>Inexpensive Gaming</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/ie.ico" />
      </Head>

      <div className={styles.bar}>
        <div className={styles.homeLink}>
          <Link href="/">
            <a>
              <h2>Inexpensive Gaming</h2>
            </a>
          </Link>
        </div>

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
        <div className={styles.productsContainer}>
          <div className={styles.container}>
            <h2>Graphics Cards</h2>
            <div className={styles.productGrid}>
              {parts.map((graphicscard) => (
                <div className={styles.productContainer}>
                  <Image src={graphicscard.imageLink} width={200} height={200} />
                  <p className={styles.productName}>{graphicscard.name}</p>
                  <Link href={graphicscard.microcenterLink}>
                    <a>
                      <h3>Microcenter</h3>
                    </a>
                  </Link>
                  <p className={styles.productName}>{graphicscard.pricing}</p>
                  <Link href={graphicscard.neweggLink}>
                    <a>
                      <h3>Newegg</h3>
                    </a>
                  </Link>
                  <p className={styles.productName}>{graphicscard.newegg}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </main>

    </div>
  )
}

export async function getServerSideProps() {
  const { db } = await connectToDatabase();

  const parts = await db
    .collection("graphicsCards")
    .find({ "manufacturer": "NVIDIA" })
    .toArray();

  return {
    props: {
      parts: JSON.parse(JSON.stringify(parts)),
    },
  };
}

