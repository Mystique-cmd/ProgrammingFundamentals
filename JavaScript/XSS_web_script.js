function sanitize(input) {
    return input
        .replace(/<script.*?>.*?<\/script>/gi, '[script removed]') // Remove script tags
        .replace(/on\w+=".*?"/gi, '[event handler removed]') // Remove event handlers
        .replace(/javascript:/gi, '[javascript removed]') // Remove javascript: URLs
}

document.getElementById("runBtn").onclick = function() {
    const userInput = document.getElementById("userInput").value;
    document.getElementById("unsafeOutput").innerHTML = userInput; // Unsafe output
    document.getElementById("safeOutput").innerHTML = sanitize(userInput); // Safe output
};