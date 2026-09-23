import React, { useState } from 'react';
import Navbar from './components/Navbar';
import Footer from './components/Footer';

// Pages
import Home from './pages/Home';
import NewScreening from './pages/NewScreening';
import TongueAnalysis from './pages/TongueAnalysis';
import SkinAnalysis from './pages/SkinAnalysis';
import SymptomsLifestyle from './pages/SymptomsLifestyle';
import AIAnalysis from './pages/AIAnalysis';
import Results from './pages/Results';
import History from './pages/History';
import Methodology from './pages/Methodology';
import DatasetsPage from './pages/DatasetsPage';
import ModelPerformance from './pages/ModelPerformance';
import About from './pages/About';

export default function App() {
  const [activePage, setActivePage] = useState('home');
  const [screeningResult, setScreeningResult] = useState(null);

  const renderPage = () => {
    switch (activePage) {
      case 'home':
        return <Home setActivePage={setActivePage} />;
      case 'new_screening':
        return <NewScreening setActivePage={setActivePage} setScreeningResult={setScreeningResult} />;
      case 'tongue':
        return <TongueAnalysis />;
      case 'skin':
        return <SkinAnalysis />;
      case 'symptoms':
        return <SymptomsLifestyle />;
      case 'ai_analysis':
        return <AIAnalysis result={screeningResult} />;
      case 'results':
        return <Results result={screeningResult} />;
      case 'history':
        return <History />;
      case 'methodology':
        return <Methodology />;
      case 'datasets':
        return <DatasetsPage />;
      case 'performance':
        return <ModelPerformance />;
      case 'about':
        return <About />;
      default:
        return <Home setActivePage={setActivePage} />;
    }
  };

  return (
    <div className="min-h-screen flex flex-col bg-slate-900 text-slate-100 font-sans">
      <Navbar activePage={activePage} setActivePage={setActivePage} />
      <main className="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {renderPage()}
      </main>
      <Footer />
    </div>
  );
}
