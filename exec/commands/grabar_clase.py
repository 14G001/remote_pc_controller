from comentarios import getCargadaRandom

async def exec(ctx, args):
    await ctx.send('Opción en desarrollo')
    if len(args) > 0:
        await ctx.send(getCargadaRandom())