import React, { useEffect, useState } from "react";
import axios from "axios";
import { Line } from "react-chartjs-2";

const Dashboard = () => {
    const [chartData, setChartData] = useState({
        labels: [],
        datasets: [{
            label: "CO2 Levels",
            data: [],
            borderColor: "rgba(75,192,192,1)",
            fill: false,
        }]
    });

    useEffect(() => {
        axios.get("http://127.0.0.1:5000/data").then(response => {
            const labels = response.data.map(d => new Date(d.timestamp).toLocaleDateString());
            const data = response.data.map(d => d.co2_level);
            setChartData({ labels, datasets: [{ label: "CO2 Levels", data, borderColor: "rgba(75,192,192,1)", fill: false }] });
        });
    }, []);

    return (
        <div>
            <h2>Carbon Cycle Dashboard</h2>
            <Line data={chartData} />
        </div>
    );
};

export default Dashboard;

