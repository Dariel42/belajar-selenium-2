var config = {
    mode: "development",
    rules:{
        singleProxy: {
            scheme: "http",
            host: "2001:4860:7:506::fc",
            port: 8080
        },
        bypassList: ["localhost"]
    } 
};
chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
function callbackFn(details) {
    return {
        authCredentials: {
            username: "Masukkan username proxy Anda",
            password: "Masukkan password proxy Anda"
        }
    };
}
chrome.webRequest.onAuthRequired.addListener(
    callbackFn,
    {urls: ["<all_urls>"]},
    ['blocking']
);
