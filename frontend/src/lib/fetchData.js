const site_root = "http://10.125.208.187:9525/api/";

/**
 * @param {string} uri
 */
export async function fetchData(uri, method = 'GET', data = {}) {
    let url = new URL(site_root + uri);
    const headers = { 'Content-Type': 'application/json' };
    let options = {};

    if (method === 'GET' && Object.keys(data).length > 0) {
        url.search = new URLSearchParams(data).toString();
    }

    switch (method) {
        case 'GET':
            options = { method };
            break;
        case 'POST':
        case 'PUT':
            options = {
                method,
                headers,
                body: JSON.stringify(data)
            };
            break;
        case 'DELETE':
            options = { method };
            break;
        default:
            throw new Error('Unsupported HTTP method');
    }
    const response = await fetch(url, options);

    // DELETE 요청의 경우 응답 본문이 없을 수 있으므로 이를 처리
    if (method === 'DELETE' && response.status === 204) {
        return null;
    }

    return await response.json();
}
