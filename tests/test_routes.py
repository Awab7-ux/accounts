
    def test_security_headers(self):
        """It should return security headers"""
        resp = self.client.get("/", environ_overrides={"wsgi.url_scheme": "https"})
        self.assertEqual(resp.headers["X-Frame-Options"], "SAMEORIGIN")
        self.assertEqual(resp.headers["X-Content-Type-Options"], "nosniff")
        self.assertIn("default-src 'self'", resp.headers["Content-Security-Policy"])
        self.assertEqual(resp.headers["Referrer-Policy"], "strict-origin-when-cross-origin")

    def test_cors_security(self):
        """It should return a CORS header"""
        resp = self.client.get("/", environ_overrides={"wsgi.url_scheme": "https"})
        self.assertEqual(resp.headers["Access-Control-Allow-Origin"], "*")
