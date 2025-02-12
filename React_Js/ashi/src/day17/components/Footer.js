import React from 'react';

function Footer() {
    return (
        <footer style={styles.footer}>
            <p>&copy; 2025 My Website. All rights reserved.</p>
        </footer>
    );
}

const styles = {
    footer: {
        backgroundColor: "#333",
        color: "white",
        padding: "10px",
        textAlign: "center", // Center the text in the footer
    }
};

export default Footer;
