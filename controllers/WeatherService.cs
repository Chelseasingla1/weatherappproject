using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

public class Weather
{
    [Key]
    public string City { get; set; }
    public float Temp { get; set; }
    public string Description { get; set; }
}

public class WeatherContext : DbContext
{
    public DbSet<Weather> Weathers { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseNpgsql("Host=localhost;Username=postgres;Password=mypassword;Database=sit331");
    }
}

public class WeatherService
{
    private readonly WeatherContext _context;

    public WeatherService()
    {
        _context = new WeatherContext();
    }

    public async Task<Weather> GetWeatherAsync(string city)
    {
        return await _context.Weathers.FindAsync(city);
    }

    public async Task AddWeatherAsync(Weather weather)
    {
        _context.Weathers.Add(weather);
        await _context.SaveChangesAsync();
    }
}

[Route("api/weather")]
[ApiController]
public class WeatherController : ControllerBase
{
    private readonly WeatherService _weatherService;

    public WeatherController()
    {
        _weatherService = new WeatherService();
    }

    // GET api/weather/{city}
    [HttpGet("{city}")]
    public async Task<ActionResult<Weather>> Get(string city)
    {
        var weather = await _weatherService.GetWeatherAsync(city);
        if (weather == null)
        {
            return NotFound();
        }
        return Ok(weather);
    }   

    // POST api/weather
    [HttpPost]
    public async Task<ActionResult<Weather>> Post(Weather weather)
    {
        await _weatherService.AddWeatherAsync(weather);

        return CreatedAtAction(nameof(Get), new { city = weather.City }, weather);
    }
}
