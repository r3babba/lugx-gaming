
(function() {
    const ANALYTICS_ENDPOINT = 'http://localhost:5001/event';

    // Generate a unique session ID for the user
    let sessionId = sessionStorage.getItem('sessionId');
    if (!sessionId) {
        sessionId = 'sess_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
        sessionStorage.setItem('sessionId', sessionId);
    }

    // --- Event Tracking Functions ---

    function sendEvent(eventType, eventData = {}) {
        const event = {
            event_time: new Date().toISOString(),
            event_type: eventType,
            page_url: window.location.href,
            session_id: sessionId,
            ...eventData
        };

        fetch(ANALYTICS_ENDPOINT, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(event),
            keepalive: true // Ensures the request is sent even if the page is being unloaded
        }).catch(error => console.error('Analytics Error:', error));
    }

    // --- Track Page View ---
    sendEvent('page_view');

    // --- Track Clicks ---
    document.addEventListener('click', function(e) {
        // We can refine this to target specific buttons or links
        const targetElement = e.target.closest('a, button');
        if (targetElement) {
            sendEvent('click', {
                element_id: targetElement.id,
                element_classes: targetElement.className,
                element_tag: targetElement.tagName,
                element_text: targetElement.textContent.trim()
            });
        }
    });

    // --- Track Scroll Depth ---
    let scrollTicking = false;
    let maxScroll = 0;
    const scrollThresholds = [25, 50, 75, 90]; // Percentages
    let triggeredScrollThresholds = new Set();

    window.addEventListener('scroll', function() {
        const scrollHeight = document.documentElement.scrollHeight;
        const clientHeight = document.documentElement.clientHeight;
        const scrollTop = window.scrollY;
        const currentScrollDepth = (scrollTop + clientHeight) / scrollHeight * 100;

        if (currentScrollDepth > maxScroll) {
            maxScroll = currentScrollDepth;
        }

        if (!scrollTicking) {
            window.requestAnimationFrame(function() {
                scrollThresholds.forEach(threshold => {
                    if (maxScroll >= threshold && !triggeredScrollThresholds.has(threshold)) {
                        sendEvent('scroll_depth', { scroll_depth: threshold });
                        triggeredScrollThresholds.add(threshold);
                    }
                });
                scrollTicking = false;
            });
            scrollTicking = true;
        }
    });


    // --- Track Time on Page ---
    let pageStartTime = Date.now();
    window.addEventListener('beforeunload', () => {
        const pageTime = (Date.now() - pageStartTime) / 1000; // in seconds
        sendEvent('page_time', { page_time: pageTime });
    });

    // --- Track Session Time ---
    // This is a simplified approach. A more robust solution would involve a backend.
    let sessionStartTime = sessionStorage.getItem('sessionStartTime');
    if (!sessionStartTime) {
        sessionStartTime = Date.now();
        sessionStorage.setItem('sessionStartTime', sessionStartTime);
    }

    // Send a heartbeat every 15 seconds to update session time
    setInterval(() => {
        const sessionTime = (Date.now() - sessionStartTime) / 1000; // in seconds
        sendEvent('session_heartbeat', { session_time: sessionTime });
    }, 15000);


})();
