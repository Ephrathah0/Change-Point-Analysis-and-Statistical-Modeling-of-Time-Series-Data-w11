import React, { useEffect, useState } from "react";
import { fetchPrices, fetchChangePoint } from "../utils/api";
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ReferenceLine } from "recharts";
import EventHighlights from "./EventHighlights";

const PriceChart = () => {
  const [prices, setPrices] = useState([]);
  const [changePoint, setChangePoint] = useState(null);

  useEffect(() => {
    const loadData = async () => {
      const data = await fetchPrices();
      const cp = await fetchChangePoint();
      setPrices(data.map(d => ({ ...d, Date: new Date(d.Date) })));
      setChangePoint(cp);
    };
    loadData();
  }, []);

  return (
    <LineChart width={1000} height={500} data={prices}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis
        dataKey="Date"
        tickFormatter={date => new Date(date).toLocaleDateString()}
        domain={["auto", "auto"]}
        type="number"
      />
      <YAxis />
      <Tooltip labelFormatter={date => new Date(date).toLocaleDateString()} />
      <Line type="monotone" dataKey="Price" stroke="#8884d8" dot={false} />
      {changePoint && (
        <ReferenceLine
          x={new Date(changePoint.date)}
          stroke="red"
          strokeDasharray="3 3"
          label="Change Point"
        />
      )}
      <EventHighlights chartData={prices} />
    </LineChart>
  );
};

export default PriceChart;
