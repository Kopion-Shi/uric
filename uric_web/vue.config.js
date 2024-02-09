module.exports = {
    devServer: {
        port: 8080,
        host: '127.0.0.1',
    },
    publicPath: process.env.NODE_ENV === 'production'
    ? '/production-sub-path/'
    : './'
}