import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
    const [articles, setArticles] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/articles/")
            .then(response => setArticles(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            <h1>Articles</h1>
            <ul>
                {articles.map(article => (
                    <li key={article.id}>{article.title}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;
