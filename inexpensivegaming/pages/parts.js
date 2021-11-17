import styles from '../styles/Home.module.css'
import Link from 'next/link'

export default function parts() {
    return (
        <main className={styles.main}>
            <div>
                <h2 className={styles.title}>What parts are you looking for?</h2>
            </div>
            <div className={styles.grid}>
                <Link href="/parts/graphics-cards">
                    <a className={styles.card}>
                        <h2>Graphics Cards &rarr;</h2>
                    </a>
                </Link>

                <Link href="/parts/cpus">
                    <a className={styles.card}>
                        <h2>CPUs &rarr;</h2>
                    </a>
                </Link>

                <Link href="/parts/motherboards">
                    <a className={styles.card}>
                        <h2>Motherboards &rarr;</h2>
                    </a>
                </Link>

                <Link href="/parts/memory">
                    <a className={styles.card}>
                        <h2>Memory &rarr;</h2>
                    </a>
                </Link>

                <Link href="/parts/power-supplies">
                    <a className={styles.card}>
                        <h2>Power Supplies &rarr;</h2>
                    </a>
                </Link>

                <Link href="/parts/cases">
                    <a className={styles.card}>
                        <h2>Cases &rarr;</h2>
                    </a>
                </Link>

                <Link href="/parts/cooling">
                    <a className={styles.card}>
                        <h2>Cooling &rarr;</h2>
                    </a>
                </Link>
            </div>
        </main>
        
    )
}