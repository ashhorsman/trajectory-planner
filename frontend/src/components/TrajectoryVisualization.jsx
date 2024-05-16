import React, { useEffect, useRef } from 'react';

const TrajectoryVisualization = ({ trajectory }) => {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');

    // Clear the canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw the trajectory as a simple line
    ctx.beginPath();
    ctx.moveTo(50, 50);
    ctx.lineTo(150, 150); // Example coordinates; replace with actual trajectory data
    ctx.stroke();
  }, [trajectory]);

  return <canvas ref={canvasRef} width={200} height={200}></canvas>;
};

export default TrajectoryVisualization;
