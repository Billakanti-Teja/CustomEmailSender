import React, { useState } from 'react';
import EmailForm from './components/EmailForm';
import Analytics from './components/Analytics';

function App() {
    return (
        <div>
            <h1>Custom Email Sender</h1>
            <EmailForm />
            <Analytics />
        </div>
    );
}

export default App;
