const data = [
    { date: "2007-04-23", value: 93.24 },
    { date: "2007-04-24", value: 95.35 },
    { date: "2007-04-25", value: 98.84 },
    { date: "2007-04-26", value: 99.92 },
    { date: "2007-04-29", value: 99.8 },
    { date: "2007-05-01", value: 99.47 },
    { date: "2007-05-02", value: 100.39 }
]

width = 500
height = 500

margin = ({ top: 20, right: 30, bottom: 30, left: 40 })

x = d3.scaleTime()
    .domain(d3.extent(data, d => d.date))
    .range([margin.left, width - margin.right])

y = d3.scaleLinear()
    .domain([0, d3.max(data, d => d.value)]).nice()
    .range([height - margin.bottom, margin.top])

xAxis = g => g
    .attr("transform", `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(x).ticks(width / 80).tickSizeOuter(0))

yAxis = g => g
    .attr("transform", `translate(${margin.left},0)`)
    .call(d3.axisLeft(y))
    .call(g => g.select(".domain").remove())
    .call(g => g.select(".tick:last-of-type text").clone()
        .attr("x", 3)
        .attr("text-anchor", "start")
        .attr("font-weight", "bold")
        .text(data.y))

line = d3.line()
    .defined(d => !isNaN(d.value))
    .x(d => x(d.date))
    .y(d => y(d.value))

const svg = d3.select("#plot");

svg.append("g")
    .call(xAxis);

svg.append("g")
    .call(yAxis);

svg.append("path")
    .datum(data)
    .attr("fill", "none")
    .attr("stroke", "steelblue")
    .attr("stroke-width", 1.5)
    .attr("stroke-linejoin", "round")
    .attr("stroke-linecap", "round")
    .attr("d", line);
