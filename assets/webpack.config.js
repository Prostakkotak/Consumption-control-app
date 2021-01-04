const path = require('path'),
    MiniCssExtractPlugin = require('mini-css-extract-plugin'),
    BrowserSyncPlugin = require('browser-sync-webpack-plugin'),
    CSSNanoPlugin = require('cssnano-webpack-plugin'),
    TerserPlugin = require('terser-webpack-plugin');

module.exports = {
    mode: 'development',
    entry: {
        styles: '@styles/styles.scss',
        report: './js/diagram-engine.js',
    },
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, '../static')
    },
    resolve: {
        alias: {
            '@styles': path.resolve(__dirname, 'styles')
        }
    },
    module: {
        rules: [
            {
                test: /\.scss$/,
                use: [
                    'style-loader',
                    MiniCssExtractPlugin.loader,
                    {
                        loader: 'css-loader',
                        options: { sourceMap: true }
                    }, {
                        loader: 'sass-loader',
                        options: { sourceMap: true }
                    }
                ]
            }
        ]
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: 'styles.css'
        }),
        new BrowserSyncPlugin({
            host: 'localhost',
            port: 3000,
            proxy: 'http://localhost:8000',
        },
        {
            injectCss: true
        })
    ],
    optimization: {
        minimizer: [
            new TerserPlugin(),
            new CSSNanoPlugin({
                cssProcessorOptions: {
                    "preset": "advanced",
                    "safe": true,
                    "map": { "inline": false },
                },
            })
        ]
    }
};