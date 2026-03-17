document.addEventListener('DOMContentLoaded', function() {
    const analyzeBtn = document.getElementById('analyzeBtn');
    const threatsTable = document.getElementById('threatsTable').querySelector('tbody');
    const totalTrafficEl = document.getElementById('totalTraffic');
    const threatCountEl = document.getElementById('threatCount');

    analyzeBtn.addEventListener('click', async function() {
        analyzeBtn.disabled = true;
        analyzeBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing...';

        try {
            const response = await fetch('/api/analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ network_data: [] })
            });

            const data = await response.json();
            
            // Update stats
            totalTrafficEl.textContent = data.total_traffic.toLocaleString();
            threatCountEl.textContent = data.threat_count;

            // Update table
            displayThreats(data.threats, data.responses);
            
        } catch (error) {
            console.error('Analysis failed:', error);
        } finally {
            analyzeBtn.disabled = false;
            analyzeBtn.innerHTML = '<i class="fas fa-play"></i> Analyze Network Traffic';
        }
    });

    function displayThreats(threats, responses) {
        threatsTable.innerHTML = '';
        threats.forEach((threat, index) => {
            const response = responses[index];
            const severityClass = threat.severity === 'HIGH' ? 'danger' : 'warning';
            
            const row = `
                <tr>
                    <td>${threat.id}</td>
                    <td><span class="badge bg-${severityClass}">${threat.severity}</span></td>
                    <td>${threat.anomaly_score.toFixed(3)}</td>
                    <td><span class="badge bg-info">${threat.action}</span></td>
                    <td>${response.action_taken}</td>
                    <td>${new Date(threat.timestamp).toLocaleTimeString()}</td>
                </tr>
            `;
            threatsTable.innerHTML += row;
        });
    }
});