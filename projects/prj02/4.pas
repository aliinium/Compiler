var
    x: integer;
    y: integer;
    add: integer;
    sub: integer;
    mul: integer;
    div: integer;

begin
    x := 100;
    y := 20;

    add := x + y;
    sub := x - y;
    mul := x * y;
    div := x / y;

    writeln(x);
    writeln(y);

    writeln('Sum x + y =');
    writeln(add);

    writeln('Sum x - y =');
    writeln(sub);

    writeln('Sum x * y =');
    writeln(mul);

    writeln('Sum x / y =');
    writeln(div);

end.
