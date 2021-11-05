import data from '/public/parts.json'

export default function graphicsCards() {
    return (
        <div>
            <h2>Graphics Cards</h2>
            {[data].map(graphicscards => (
                <h2>{graphicscards.graphicscard}</h2>
            ))}
        </div>  
    )
}

