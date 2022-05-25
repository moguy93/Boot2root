int     main(int ac, char **av)
{
    char    buff[128];

    if (ac <= 1)
        return (1);

    strcpy(buff, av[1]);
    puts(buff);
    
    return (0);
}