import axios from "axios";
import React, { useState } from "react";

function EmailForm() {
    const [file, setFile] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("file", file);

        const response = await axios.post("http://localhost:5000/upload", formData);
        console.log(response.data);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="file" onChange={(e) => setFile(e.target.files[0])} />
            <button type="submit">Upload Emails</button>
        </form>
    );
}

export default EmailForm;
