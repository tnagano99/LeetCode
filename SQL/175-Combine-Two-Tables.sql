Select a.Firstname, a.LastName, b.City, b.State
From Person as a
left join
Address as b
on a.PersonId = b.PersonId