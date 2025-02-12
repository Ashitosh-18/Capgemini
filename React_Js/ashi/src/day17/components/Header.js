import React from "react";

function Header() {
  return (
    <header style={styles.header}>
      <h1 style={styles.siteTitle}>My Website</h1> {/* Left-aligned text */}
      <nav>
        <ul style={styles.navList}>
          <li><a href="#" style={styles.navLink}>Home</a></li>
          <li><a href="#" style={styles.navLink}>About</a></li>
          <li><a href="#" style={styles.navLink}>Contact</a></li>
        </ul>
      </nav>
    </header>
  );
}

const styles = {
  header: {
    backgroundColor: "#333",
    color: "white",
    padding: "10px",
    display: "flex",
    justifyContent: "space-between", // Align left and right content
    alignItems: "center", // Vertically center
  },
  siteTitle: {
    margin: 0, // Remove default margin from <h1>
  },
  navList: {
    listStyleType: "none",
    padding: 0,
    display: "flex",
    gap: "15px", // Adds spacing between links
  },
  navLink: {
    color: "white",
    textDecoration: "none",
    fontSize: "18px",
  },
};

export default Header;
