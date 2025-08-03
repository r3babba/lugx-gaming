const backendUrl = 'http://localhost:5000/event'; // Adjust when deployed

const sessionId = Math.random().toString(36).substring(2, 15);
let pageStartTime = Date.now();

function sendEvent(event) {
  fetch(backendUrl, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(event)
  });
}

// Page View event on load
window.addEventListener('load', () => {
  sendEvent({
    event_type: 'page_view',
    page_url: window.location.href,
    session_id: sessionId,
    scroll_depth: 0,
    page_time: 0,
    session_time: 0,
    event_time: new Date().toISOString()
  });
});

// Click event
document.getElementById('clickBtn').addEventListener('click', () => {
  sendEvent({
    event_type: 'click',
    page_url: window.location.href,
    session_id: sessionId,
    scroll_depth: 0,
    page_time: (Date.now() - pageStartTime) / 1000,
    session_time: 0,
    event_time: new Date().toISOString()
  });
});

// Scroll Depth event - send max scroll every 5 seconds
let maxScrollPercent = 0;
window.addEventListener('scroll', () => {
  let scrollTop = window.scrollY;
  let docHeight = document.documentElement.scrollHeight - window.innerHeight;
  let scrollPercent = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
  if(scrollPercent > maxScrollPercent) {
    maxScrollPercent = scrollPercent;
  }
});

setInterval(() => {
  if(maxScrollPercent > 0) {
    sendEvent({
      event_type: 'scroll',
      page_url: window.location.href,
      session_id: sessionId,
      scroll_depth: Math.round(maxScrollPercent),
      page_time: (Date.now() - pageStartTime) / 1000,
      session_time: 0,
      event_time: new Date().toISOString()
    });
    maxScrollPercent = 0;
  }
}, 5000);

// Session time on unload
window.addEventListener('beforeunload', () => {
  const sessionTime = (Date.now() - pageStartTime) / 1000;
  navigator.sendBeacon(backendUrl, JSON.stringify({
    event_type: 'session_time',
    page_url: window.location.href,
    session_id: sessionId,
    scroll_depth: 0,
    page_time: sessionTime,
    session_time: sessionTime,
    event_time: new Date().toISOString()
  }));
});
