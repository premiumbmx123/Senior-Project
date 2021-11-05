import data from '/public/parts.json'

export default function cpus() {
    return (
        <div>
            <h2>CPUs</h2>
            {[data].map(cpus => (
                <h2>{cpus.cpu}</h2>
            ))}
        </div>  
    )
}
