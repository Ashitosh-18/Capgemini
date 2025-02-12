import './App.css';
import Header from './day17/components/Header';
import Footer from './day17/components/Footer';
import Body from './day17/components/Body';
import InterestCalculator from './day17/intrest_calc';

function App() {
  return (
    <div className="App">
      <Header/>
      <Body/>
      <InterestCalculator/>
      <br/>
      <Footer/>
      <a className="App-link" href="https://reactjs.org" target="_blank" rel="noopener noreferrer"> Learn React </a>
    </div>
  );
}

export default App;
